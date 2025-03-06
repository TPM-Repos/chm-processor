![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

_T_
    The type of the condition to create. This type must inherit from [ComponentTaskReleaseCondition](topic6647.md).

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Add<T>(String) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6690.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskReleaseConditions Class](topic6682.md) > [Add Method](topic6688.md) : Add<T>(String) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_title_
    The title of the condition to create.

Glossary Item Box

Creates a new [ComponentTaskReleaseCondition](topic6647.md) of type T and adds it to the collection. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function Add(Of T As [ComponentTaskReleaseCondition](topic6647.md))( _
       ByVal _title_ As String _
    ) As T  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskReleaseConditions](topic6682.md)
    Dim title As String
    Dim value As T
     
    value = instance.Add(Of T)(title)  
  
C#|   
---|---  
      
    
    public T Add<T>( 
       string _title_
    )
    where T: [ComponentTaskReleaseCondition](topic6647.md)  
  
#### Parameters

 _title_
    The title of the condition to create.

#### Type Parameters

_T_
    The type of the condition to create. This type must inherit from [ComponentTaskReleaseCondition](topic6647.md).

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
