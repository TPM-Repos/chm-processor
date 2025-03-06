Rule Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectVariable Class](topic4927.md) : Rule Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Gets/sets the rule which governs the variable's value. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustOverride Property Rule As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectVariable](topic4927.md)
    Dim value As String
     
    instance.Rule = value
     
    value = instance.Rule  
  
C#|   
---|---  
      
    
    public abstract string Rule {get; set;}  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectVariable Class](topic4927.md)   
[ProjectVariable Members](topic4928.md)


