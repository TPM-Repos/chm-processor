Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
OnValueChanged Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Forms Namespace](topic7266.md) > [ControlBase Class](topic7698.md) : OnValueChanged Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_e_
    The event data.

Glossary Item Box

Raises the [OnValueChanged](topic7715.md) event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Protected Overridable Sub OnValueChanged( _
       ByVal _e_ As [ValueChangedEventArgs](topic9575.md) _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ControlBase](topic7698.md)
    Dim e As [ValueChangedEventArgs](topic9575.md)
     
    instance.OnValueChanged(e)  
  
C#|   
---|---  
      
    
    protected virtual void OnValueChanged( 
       [ValueChangedEventArgs](topic9575.md) _e_
    )  
  
#### Parameters

 _e_
    The event data.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ControlBase Class](topic7698.md)   
[ControlBase Members](topic7699.md)


