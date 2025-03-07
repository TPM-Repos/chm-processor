Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Close Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [SettingsPage Class](topic935.md) : Close Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_save_
    True if the settings on page are to be stored.

Glossary Item Box

When overridden by a derived class, performs closing logic specific to the derived page. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overridable Sub Close( _
       ByVal _save_ As Boolean _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SettingsPage](topic935.md)
    Dim save As Boolean
     
    instance.Close(save)  
  
C#|   
---|---  
      
    
    public virtual void Close( 
       bool _save_
    )  
  
#### Parameters

 _save_
    True if the settings on page are to be stored.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SettingsPage Class](topic935.md)   
[SettingsPage Members](topic936.md)


