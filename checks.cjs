const assert=require('node:assert/strict'),fs=require('node:fs'),{score,stats}=require('./dist/logic.js');
const d=JSON.parse(fs.readFileSync('dist/data.json'));assert.equal(d.questions.length,31);assert.equal(new Set(d.questions.map(q=>q.id)).size,31);assert.equal(d.cases.length,4);
for(const c of d.cases){assert.equal(Object.keys(d.answers[c.id]).length,31);for(const q of d.questions){let a=d.answers[c.id][q.id];assert.ok(a.ref&&a.text);assert.ok(d.method.status[a.status]);assert.ok(a.grade===null||(q.dimension==='Management'&&Number.isInteger(a.grade)&&a.grade>=0&&a.grade<=3));if(a.status==='gap')assert.ok(a.missing)}const s=stats(d,c.id);assert.equal(s.total,20);assert.equal(s.num+s.qual+s.plan+s.gap,20);console.log(c.id,s)}
for(const [x,b,t,dir,want] of [[80,100,60,'lower',50],[50,100,60,'lower',100],[120,100,60,'lower',0],[80,60,100,'higher',50],[120,60,100,'higher',100],[40,60,100,'higher',0]])assert.equal(score(x,b,t,dir).value,want);
for(const args of [['',100,60,'lower'],[80,60,60,'lower'],[80,60,100,'lower'],[NaN,100,60,'lower']])assert.ok(score(...args).error);
assert.equal(d.answers.mercedes.W2.number.actual,8);assert.equal(d.answers.hoeren.S3.number.actual,270);console.log('Datenintegrität und Rechenlogik geprüft.');

assert.equal(d.questions.filter(q=>q.dimension==='Ökologisch').length,8);
assert.equal(d.answers.mercedes.O8.status,'plan');
assert.equal(d.answers.mercedes.O8.number,null);
assert.match(d.answers.mercedes.O8.text,/weniger als 1 m²/);
for(const c of d.cases) assert.equal(d.answers[c.id].O7.status,'gap');
assert.match(d.questions.find(q=>q.id==='O5').format,/Trinkwasseranteil/);
