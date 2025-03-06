![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Register(String,String,Type) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic7106.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.EventFlow Namespace](topic6871.md) > [NodeOutputCollection Class](topic7087.md) > [Register Method](topic7105.md) : Register(String,String,Type) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the output to create.

_description_
    The user-friendly description of the output.

_valueType_
    The type of the value this output stores.

Glossary Item Box

Adds a new output to the collection. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function Register( _
       ByVal _name_ As String, _
       ByVal _description_ As String, _
       ByVal _valueType_ As Type _
    ) As [NodeOutput](topic7074.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [NodeOutputCollection](topic7087.md)
    Dim name As String
    Dim description As String
    Dim valueType As Type
    Dim value As [NodeOutput](topic7074.md)
     
    value = instance.Register(name, description, valueType)  
  
C#|   
---|---  
      
    
    public [NodeOutput](topic7074.md) Register( 
       string _name_ ,
       string _description_ ,
       Type _valueType_
    )  
  
#### Parameters

 _name_
    The name of the output to create.
_description_
    The user-friendly description of the output.
_valueType_
    The type of the value this output stores.

#### Return Value

The newly created output.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[NodeOutputCollection Class](topic7087.md)   
[NodeOutputCollection Members](topic7088.md)   
[Overload List](topic7105.md)

©2024 DriveWorks Ltd. All Rights Reserved.
