![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
NotifyEvaluatedAsDrivenAlternative Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic6134.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components Namespace](topic6089.md) > [IReleaseTracker Interface](topic6119.md) : NotifyEvaluatedAsDrivenAlternative Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_alternativeId_
    The unique identifier of the driven alternative.

_alternativeMasterPath_
    The path to the file on which the driven alternative was based.

_alternativeTargetPath_
    The path to the driven alternative.

Glossary Item Box

Called when the current component is determined to need swapping for a driven alternative. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub NotifyEvaluatedAsDrivenAlternative( _
       ByVal _alternativeId_ As Guid, _
       ByVal _alternativeMasterPath_ As String, _
       ByVal _alternativeTargetPath_ As String _
    )   
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [IReleaseTracker](topic6119.md)
    Dim alternativeId As Guid
    Dim alternativeMasterPath As String
    Dim alternativeTargetPath As String
     
    instance.NotifyEvaluatedAsDrivenAlternative(alternativeId, alternativeMasterPath, alternativeTargetPath)  
  
C#|   
---|---  
      
    
    void NotifyEvaluatedAsDrivenAlternative( 
       Guid _alternativeId_ ,
       string _alternativeMasterPath_ ,
       string _alternativeTargetPath_
    )  
  
#### Parameters

 _alternativeId_
    The unique identifier of the driven alternative.
_alternativeMasterPath_
    The path to the file on which the driven alternative was based.
_alternativeTargetPath_
    The path to the driven alternative.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[IReleaseTracker Interface](topic6119.md)   
[IReleaseTracker Members](topic6120.md)

©2024 DriveWorks Ltd. All Rights Reserved.
