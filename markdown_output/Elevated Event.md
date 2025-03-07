Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Elevated Event   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ISettingsManager Interface](topic442.md) : Elevated Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the settings manager has been elevated. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Event Elevated As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISettingsManager](topic442.md)
    Dim handler As EventHandler
     
    AddHandler instance.Elevated, handler  
  
C#|   
---|---  
      
    
    event EventHandler Elevated  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISettingsManager Interface](topic442.md)   
[ISettingsManager Members](topic443.md)


