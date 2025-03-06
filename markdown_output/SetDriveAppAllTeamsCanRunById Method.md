![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetDriveAppAllTeamsCanRunById Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic3222.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupProjects Class](topic3190.md) : SetDriveAppAllTeamsCanRunById Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_id_
    The unique identifier of the DriveApp to update.

_allTeamsCanRun_
    True if all teams can run the DriveApp, otherwise custom security is applied.

Glossary Item Box

Updates whether all teams can run the DriveApp, or whether custom security is applied. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function SetDriveAppAllTeamsCanRunById( _
       ByVal _id_ As Guid, _
       ByVal _allTeamsCanRun_ As Boolean _
    ) As Boolean  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [GroupProjects](topic3190.md)
    Dim id As Guid
    Dim allTeamsCanRun As Boolean
    Dim value As Boolean
     
    value = instance.SetDriveAppAllTeamsCanRunById(id, allTeamsCanRun)  
  
C#|   
---|---  
      
    
    public bool SetDriveAppAllTeamsCanRunById( 
       Guid _id_ ,
       bool _allTeamsCanRun_
    )  
  
#### Parameters

 _id_
    The unique identifier of the DriveApp to update.
_allTeamsCanRun_
    True if all teams can run the DriveApp, otherwise custom security is applied.

#### Return Value

True if successfully updated.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[GroupProjects Class](topic3190.md)   
[GroupProjects Members](topic3191.md)

©2024 DriveWorks Ltd. All Rights Reserved.
