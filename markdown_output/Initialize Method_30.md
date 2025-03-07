Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Initialize Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [SettingsPage Class](topic935.md) : Initialize Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_application_
    The host application.

_settingsManager_
    The settings manager.

Glossary Item Box

Initializes the page with core objects. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub Initialize( _
       ByVal _application_ As [IApplication](topic24.md), _
       ByVal _settingsManager_ As [ISettingsManager](topic442.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SettingsPage](topic935.md)
    Dim application As [IApplication](topic24.md)
    Dim settingsManager As [ISettingsManager](topic442.md)
     
    instance.Initialize(application, settingsManager)  
  
C#|   
---|---  
      
    
    public void Initialize( 
       [IApplication](topic24.md) _application_ ,
       [ISettingsManager](topic442.md) _settingsManager_
    )  
  
#### Parameters

 _application_
    The host application.
_settingsManager_
    The settings manager.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SettingsPage Class](topic935.md)   
[SettingsPage Members](topic936.md)


