---
title: Conditional Rendering in React
date: 2023-12-01
tags: 
aliases: 
feed: hide
published: true
---

When rendering conditionally, Do it around the main component. Favor simple conditional rendering expressions, and extract each layer into its own component to maintain readability. ex
```
function LogicRouter({props}){
	if(data === 'foo'){ 
		return <Sub1 />
	}
	if(data === 'bar'){
		return <Sub2 />
	}

	return <DefaultComponent />
}
```
which can be used in higher level components
```
function Main(){
	const data = getData()

	return(
		<>
		  <div>some stuff</div>
		  <LogicRouter props={data} />
		<>
	)
}
```

>- If only boolean, can do `<Container>{condition && <Something />}</Container>`
>- If relatively simple and only 2 options, can often get away with a ternary
>- If more than 2 options, can potentially use a instantly-executed inline function or a separate component or whatever allows you to do multiple early returns
>- If more complex in general, maybe a separate component

### Conditional Render with Guard Clause
```ts
const Foo = () => {
  if(!data) {
    return <div>No Data</div>
  }

  return (
    // main component stuff here
  )
}
```

__Note: Put Guard Clauses at the top of the function__ 
### Switch Statement Render
```ts
return (switch(ProfileType)
  case 'CompanyContact':
     return <CompanyContact {props} />
  case 'BrokerProfile':
     return <BrokerProfile {props} />
  default:
     return <GenericProfile {props/>
)
```