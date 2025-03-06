![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NotifyEvaluatedAsStandardAlternativeWithInvalidPath Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [IReleaseTracker Interface](topic6119.md) : NotifyEvaluatedAsStandardAlternativeWithInvalidPath Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_invalidPath_
    The invalid path to the standard alternative.

Glossary Item Box

Called when the current component is determined to need swapping for a standard alternative that has an invalid full path. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub NotifyEvaluatedAsStandardAlternativeWithInvalidPath( _
       ByVal _invalidPath_ As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IReleaseTracker](topic6119.md)
    Dim invalidPath As String
     
    instance.NotifyEvaluatedAsStandardAlternativeWithInvalidPath(invalidPath)  
  
C#|   
---|---  
      
    
    void NotifyEvaluatedAsStandardAlternativeWithInvalidPath( 
       string _invalidPath_
    )  
  
#### Parameters

 _invalidPath_
    The invalid path to the standard alternative.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IReleaseTracker Interface](topic6119.md)   
[IReleaseTracker Members](topic6120.md)


