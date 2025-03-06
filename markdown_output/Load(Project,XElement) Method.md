![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Load(Project,XElement) Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6312.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [ReleaseComponentsResults Class](topic6300.md) > [Load Method](topic6310.md) : Load(Project,XElement) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_project_
    The project loading the results.

_savedResults_
    The saved release results.

Glossary Item Box

Loads the released component results from the given XML. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Shared Function Load( _
       ByVal _project_ As [Project](topic3859.md), _
       ByVal _savedResults_ As XElement _
    ) As [ReleaseComponentsResults](topic6300.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim project As [Project](topic3859.md)
    Dim savedResults As XElement
    Dim value As [ReleaseComponentsResults](topic6300.md)
     
    value = [ReleaseComponentsResults](topic6300.md).Load(project, savedResults)  
  
C#|   
---|---  
      
    
    public static [ReleaseComponentsResults](topic6300.md) Load( 
       [Project](topic3859.md) _project_ ,
       XElement _savedResults_
    )  
  
#### Parameters

 _project_
    The project loading the results.
_savedResults_
    The saved release results.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ReleaseComponentsResults Class](topic6300.md)   
[ReleaseComponentsResults Members](topic6301.md)   
[Overload List](topic6310.md)

©2024 DriveWorks Ltd. All Rights Reserved.
