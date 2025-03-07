Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CanRequestElevation Property   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ISettingsManager Interface](topic442.md) : CanRequestElevation Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Returns true if the settings manager is capable of requesting elevation for access to privileged settings. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    ReadOnly Property CanRequestElevation As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISettingsManager](topic442.md)
    Dim value As Boolean
     
    value = instance.CanRequestElevation  
  
C#|   
---|---  
      
    
    bool CanRequestElevation {get;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISettingsManager Interface](topic442.md)   
[ISettingsManager Members](topic443.md)


