Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetDriveApps Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupProjects Class](topic3190.md) : GetDriveApps Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Returns all the DriveApps in the group. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function GetDriveApps() As [DriveAppDetails()](topic2750.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupProjects](topic3190.md)
    Dim value() As [DriveAppDetails](topic2750.md)
     
    value = instance.GetDriveApps()  
  
C#|   
---|---  
      
    
    public [DriveAppDetails[]](topic2750.md) GetDriveApps()  
  
#### Return Value

An array of [DriveAppDetails](topic2750.md).

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupProjects Class](topic3190.md)   
[GroupProjects Members](topic3191.md)


