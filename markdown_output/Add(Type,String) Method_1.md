![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add(Type,String) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6473.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskCollection Class](topic6466.md) : Add(Type,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_type_
    The type of the task to create.

_name_
    The name of the task to create.

Glossary Item Box

Adds a new task to the collection and returns the newly created task. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function Add( _
       ByVal _type_ As Type, _
       ByVal _name_ As String _
    ) As [ComponentTask](topic6407.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskCollection](topic6466.md)
    Dim type As Type
    Dim name As String
    Dim value As [ComponentTask](topic6407.md)
     
    value = instance.Add(type, name)  
  
C#|   
---|---  
      
    
    public [ComponentTask](topic6407.md) Add( 
       Type _type_ ,
       string _name_
    )  
  
#### Parameters

 _type_
    The type of the task to create.
_name_
    The name of the task to create.

#### Return Value

The newly created task, or a null reference (Nothing in VB) if the creation of the task fails.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ComponentTaskCollection Class](topic6466.md)   
[ComponentTaskCollection Members](topic6467.md)

©2024 DriveWorks Ltd. All Rights Reserved.
