Rule Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectRuleEvent Class](topic4738.md) : Rule Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

The formula for this event. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public ReadOnly Property Rule As String  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectRuleEvent](topic4738.md)
    Dim value As String
     
    value = instance.Rule  
  
C#|   
---|---  
      
    
    public string Rule {get;}  
  
# Remarks

Potentially null as not every event is based on a rule (such as a value setting events).

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectRuleEvent Class](topic4738.md)   
[ProjectRuleEvent Members](topic4739.md)


