ValueChanged Event   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectVariable Class](topic4927.md) : ValueChanged Event  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Raised when the value of the variable changes. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Event ValueChanged As EventHandler  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectVariable](topic4927.md)
    Dim handler As EventHandler
     
    AddHandler instance.ValueChanged, handler  
  
C#|   
---|---  
      
    
    public event EventHandler ValueChanged  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectVariable Class](topic4927.md)   
[ProjectVariable Members](topic4928.md)


