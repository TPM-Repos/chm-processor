![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateComponent(Type,String) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3033.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupCapturedComponents Class](topic3022.md) > [CreateComponent Method](topic3031.md) : CreateComponent(Type,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_type_
    The type of component to create.

_path_
    The path to the file represented by the component.

Glossary Item Box

Creates and returns a new component of the specified type without registering it with the group. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function CreateComponent( _
       ByVal _type_ As Type, _
       ByVal _path_ As String _
    ) As [CapturedComponent](topic6147.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupCapturedComponents](topic3022.md)
    Dim type As Type
    Dim path As String
    Dim value As [CapturedComponent](topic6147.md)
     
    value = instance.CreateComponent(type, path)  
  
C#|   
---|---  
      
    
    public [CapturedComponent](topic6147.md) CreateComponent( 
       Type _type_ ,
       string _path_
    )  
  
#### Parameters

 _type_
    The type of component to create.
_path_
    The path to the file represented by the component.

#### Return Value

An instance of type derived from [DriveWorks.Components.CapturedComponent](topic6147.md) which represents a component of the specified type

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupCapturedComponents Class](topic3022.md)   
[GroupCapturedComponents Members](topic3023.md)   
[Overload List](topic3031.md)

©2024 DriveWorks Ltd. All Rights Reserved.
