![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
RegisterIArrayValueProperty(String,String) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [FlowProperties Class](topic10905.md) > [RegisterIArrayValueProperty Method](topic10925.md) : RegisterIArrayValueProperty(String,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the property.

_description_
    The description of the property.

Glossary Item Box

Creates a new specification flow property which can store IArrayValue data. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function RegisterIArrayValueProperty( _
       ByVal _name_ As String, _
       ByVal _description_ As String _
    ) As [FlowProperty(Of IArrayValue)](topic10978.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [FlowProperties](topic10905.md)
    Dim name As String
    Dim description As String
    Dim value As [FlowProperty(Of IArrayValue)](topic10978.md)
     
    value = instance.RegisterIArrayValueProperty(name, description)  
  
C#|   
---|---  
      
    
    public [FlowProperty<IArrayValue>](topic10978.md) RegisterIArrayValueProperty( 
       string _name_ ,
       string _description_
    )  
  
#### Parameters

 _name_
    The name of the property.
_description_
    The description of the property.

#### Return Value

A new specification flow property.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[FlowProperties Class](topic10905.md)   
[FlowProperties Members](topic10906.md)   
[Overload List](topic10925.md)


