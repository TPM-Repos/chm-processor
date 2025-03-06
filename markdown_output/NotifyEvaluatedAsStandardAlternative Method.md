![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NotifyEvaluatedAsStandardAlternative Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [IReleaseTracker Interface](topic6119.md) : NotifyEvaluatedAsStandardAlternative Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_alternativePath_
    

Glossary Item Box

Called when the current component is determined to need swapping for a standard alternative. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub NotifyEvaluatedAsStandardAlternative( _
       ByVal _alternativePath_ As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IReleaseTracker](topic6119.md)
    Dim alternativePath As String
     
    instance.NotifyEvaluatedAsStandardAlternative(alternativePath)  
  
C#|   
---|---  
      
    
    void NotifyEvaluatedAsStandardAlternative( 
       string _alternativePath_
    )  
  
#### Parameters

 _alternativePath_
    

# ![](dotnetimages/collapse.gif)Remarks

Note, if the current component is a root component, i.e. it doesn't have a parent, then the receipt of this call indicates that the rule for the component is invalid because a root component can't be swapped for an alternative.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IReleaseTracker Interface](topic6119.md)   
[IReleaseTracker Members](topic6120.md)


