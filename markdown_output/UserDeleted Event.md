UserDeleted Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) : UserDeleted Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a user is successfully deleted. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event UserDeleted As [UserChangedEventHandler](topic5936.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim handler As [UserChangedEventHandler](topic5936.md)
     
    AddHandler instance.UserDeleted, handler  
  
C#|   
---|---  
      
    
    public event [UserChangedEventHandler](topic5936.md) UserDeleted  
  
# Event Data

The event handler receives an argument of type [UserChangedEventArgs](topic5800.md) containing data related to this event. The following **UserChangedEventArgs** properties provide information specific to this event.

Property| Description  
---|---  
[User](topic5808.md)| Gets the user that was changed.   
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)


