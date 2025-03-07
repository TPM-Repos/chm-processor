Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
DeactivateCore Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [SettingsPage Class](topic935.md) : DeactivateCore Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_cancel_
    Set to true by the overridden method to cancel the navigation action if desired.

Glossary Item Box

When overridden by a derived class, performs deactivation logic specific to the derived page. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Sub DeactivateCore( _
       ByRef _cancel_ As Boolean _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SettingsPage](topic935.md)
    Dim cancel As Boolean
     
    instance.DeactivateCore(cancel)  
  
C#|   
---|---  
      
    
    protected virtual void DeactivateCore( 
       ref bool _cancel_
    )  
  
#### Parameters

 _cancel_
    Set to true by the overridden method to cancel the navigation action if desired.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SettingsPage Class](topic935.md)   
[SettingsPage Members](topic936.md)


