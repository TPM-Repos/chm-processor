![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add(Type,String) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6689.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskReleaseConditions Class](topic6682.md) > [Add Method](topic6688.md) : Add(Type,String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_type_
    The type of the condition to create. This type must inherit from [ComponentTaskReleaseCondition](topic6647.md).

_title_
    The title of the condition to create.

Glossary Item Box

Creates a new [ComponentTaskReleaseCondition](topic6647.md) of the given type and adds it to the collection. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function Add( _
       ByVal _type_ As Type, _
       ByVal _title_ As String _
    ) As [ComponentTaskReleaseCondition](topic6647.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskReleaseConditions](topic6682.md)
    Dim type As Type
    Dim title As String
    Dim value As [ComponentTaskReleaseCondition](topic6647.md)
     
    value = instance.Add(type, title)  
  
C#|   
---|---  
      
    
    public [ComponentTaskReleaseCondition](topic6647.md) Add( 
       Type _type_ ,
       string _title_
    )  
  
#### Parameters

 _type_
    The type of the condition to create. This type must inherit from [ComponentTaskReleaseCondition](topic6647.md).
_title_
    The title of the condition to create.

#### Return Value

The newly created condition.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ComponentTaskReleaseConditions Class](topic6682.md)   
[ComponentTaskReleaseConditions Members](topic6683.md)   
[Overload List](topic6688.md)

©2024 DriveWorks Ltd. All Rights Reserved.
