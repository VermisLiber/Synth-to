
void main() => runApp (new MaterialApp(

home: new MyApp(),

)); 

class MyApp extends Statefulwidget {

@override

_MyAppState createState() => MyAppState();

}

class _MyAppState extends State<MyApp> 
{ 
  @override
  
  Widget build(BuildContext context) {

return Scaffold();

}

}

 @override

_MyAppState createState() => _MyAppState();

}

class MyAppState extends State<MyApp> {

@override

Widget build (BuildContext context) {

return Scaffold(

appBar: AppBar(

title:Text('Appbar Demo'),
  
  ),
  
  );
  
}
  
}

@override

_MyAppState createState() =>_MyAppState();

}


class _MyAppState extends State<MyApp> {
  
  @override
  
  Widget build(BuildContext context) {
    
    
    return Scaffold(
      
      appBar:AppBar(
        
        leading:IconButton(
          
          icon:Icon(Icons.menu),
          
          onpressed: () {
            
            print('Icon Button Click');
            
          },
          
        ),
        
        title:Text('Appbar Demo'),



        actions: <Widget>[
          
          IconButton(
            
            icon:Icon(Icons.search),
            
            onPressed: () {},
            )
          ],
        ),
      );

    
class MyAppState extends StatefulWidget {
  
 @override
  
 _MyAppState createState() =>_MyappState();
  
}
    
class _MyAppState extends State<MyApp> {
  @override
 
    
  Widget build(BuildContext context) {
  
  return Scaffold(
    
    appBar: AppBar(...),
    
    body:Center(
      
      child:Text(
        
        'Text Promoter',
        
        style:TextStyle(
          
          fontSize:28.0,
          
          colour:Colours.red,
          )
          
     
        
        ),
      ),
  

