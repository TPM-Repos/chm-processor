       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
TryGetDriveApp(String,DriveAppDetails) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupProjects Class](topic3190.md) > [TryGetDriveApp Method](topic3227.md) : TryGetDriveApp(String,DriveAppDetails) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_driveAppAlias_
    The alias name of the DriveApp.

_driveAppDetails_
    

Glossary Item Box

Gets a DriveApp with the specified alias name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Function TryGetDriveApp( _
       ByVal _driveAppAlias_ As String, _
       ByRef _driveAppDetails_ As [DriveAppDetails](topic2750.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupProjects](topic3190.md)
    Dim driveAppAlias As String
    Dim driveAppDetails As [DriveAppDetails](topic2750.md)
    Dim value As Boolean
     
    value = instance.TryGetDriveApp(driveAppAlias, driveAppDetails)  
  
C#|   
---|---  
      
    
    public bool TryGetDriveApp( 
       string _driveAppAlias_ ,
       ref [DriveAppDetails](topic2750.md) _driveAppDetails_
    )  
  
#### Parameters

 _driveAppAlias_
    The alias name of the DriveApp.
_driveAppDetails_
    

#### Return Value

The [DriveAppDetails](topic2750.md) for the DriveApp with the specified alias name, or a null reference if no DriveApp with the given name exists.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupProjects Class](topic3190.md)   
[GroupProjects Members](topic3191.md)   
[Overload List](topic3227.md)


