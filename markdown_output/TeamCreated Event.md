TeamCreated Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [GroupSecurity Class](topic3282.md) : TeamCreated Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when a team is created. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event TeamCreated As [TeamChangedEventHandler](topic5935.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [GroupSecurity](topic3282.md)
    Dim handler As [TeamChangedEventHandler](topic5935.md)
     
    AddHandler instance.TeamCreated, handler  
  
C#|   
---|---  
      
    
    public event [TeamChangedEventHandler](topic5935.md) TeamCreated  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[GroupSecurity Class](topic3282.md)   
[GroupSecurity Members](topic3283.md)


