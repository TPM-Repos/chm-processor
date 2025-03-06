![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetTransitionsByTitle Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic11796.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Transitions Class](topic11787.md) : GetTransitionsByTitle Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_title_
    The title of the transitions to retrieve.

Glossary Item Box

Gets the transitions in the collection with the specified title. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetTransitionsByTitle( _
       ByVal _title_ As String _
    ) As [Transition()](topic11757.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [Transitions](topic11787.md)
    Dim title As String
    Dim value() As [Transition](topic11757.md)
     
    value = instance.GetTransitionsByTitle(title)  
  
C#|   
---|---  
      
    
    public [Transition[]](topic11757.md) GetTransitionsByTitle( 
       string _title_
    )  
  
#### Parameters

 _title_
    The title of the transitions to retrieve.

#### Return Value

An array of transitions.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[Transitions Class](topic11787.md)   
[Transitions Members](topic11788.md)

©2024 DriveWorks Ltd. All Rights Reserved.
