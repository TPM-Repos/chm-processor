![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetCanExecute Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic9813.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupMaintenance Namespace](topic9628.md) > [CopyGroupTeamAction Class](topic9806.md) : GetCanExecute Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_useCache_
    Whether or not he value needs to be re-evaluated from a last attempt.

Glossary Item Box

Checks to see if the action can be executed or not. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overrides Function GetCanExecute( _
       ByVal _useCache_ As Boolean _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [CopyGroupTeamAction](topic9806.md)
    Dim useCache As Boolean
    Dim value As Boolean
     
    value = instance.GetCanExecute(useCache)  
  
C#|   
---|---  
      
    
    public override bool GetCanExecute( 
       bool _useCache_
    )  
  
#### Parameters

 _useCache_
    Whether or not he value needs to be re-evaluated from a last attempt.

#### Return Value

True if it can execute.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[CopyGroupTeamAction Class](topic9806.md)   
[CopyGroupTeamAction Members](topic9807.md)

©2024 DriveWorks Ltd. All Rights Reserved.
