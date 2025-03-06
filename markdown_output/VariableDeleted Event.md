VariableDeleted Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectVariables Class](topic5010.md) : VariableDeleted Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a variable is deleted. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event VariableDeleted As [VariableChangedEventHandler](topic5938.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectVariables](topic5010.md)
    Dim handler As [VariableChangedEventHandler](topic5938.md)
     
    AddHandler instance.VariableDeleted, handler  
  
C#|   
---|---  
      
    
    public event [VariableChangedEventHandler](topic5938.md) VariableDeleted  
  
# Event Data

The event handler receives an argument of type [VariableEventArgs](topic5874.md) containing data related to this event. The following **VariableEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[Variable](topic5884.md)| Gets the constant that was changed.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectVariables Class](topic5010.md)   
[ProjectVariables Members](topic5011.md)


