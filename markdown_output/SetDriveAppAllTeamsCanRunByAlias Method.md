       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SetDriveAppAllTeamsCanRunByAlias Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupProjects Class](topic3190.md) : SetDriveAppAllTeamsCanRunByAlias Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_appAlias_
    The unique alias name of the DriveApp to update.

_allTeamsCanRun_
    True if all teams can run the DriveApp, otherwise custom security is applied.

Glossary Item Box

Updates whether all teams can run the DriveApp, or whether custom security is applied. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function SetDriveAppAllTeamsCanRunByAlias( _
       ByVal _appAlias_ As String, _
       ByVal _allTeamsCanRun_ As Boolean _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupProjects](topic3190.md)
    Dim appAlias As String
    Dim allTeamsCanRun As Boolean
    Dim value As Boolean
     
    value = instance.SetDriveAppAllTeamsCanRunByAlias(appAlias, allTeamsCanRun)  
  
C#|   
---|---  
      
    
    public bool SetDriveAppAllTeamsCanRunByAlias( 
       string _appAlias_ ,
       bool _allTeamsCanRun_
    )  
  
#### Parameters

 _appAlias_
    The unique alias name of the DriveApp to update.
_allTeamsCanRun_
    True if all teams can run the DriveApp, otherwise custom security is applied.

#### Return Value

True if successfully updated.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupProjects Class](topic3190.md)   
[GroupProjects Members](topic3191.md)


