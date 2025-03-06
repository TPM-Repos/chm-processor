WillExecute Property   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupMaintenance Namespace](topic9628.md) > [ProcessActionBase Class](topic9935.md) : WillExecute Property  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Returns whether or not this action wants to execute. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overridable ReadOnly Property WillExecute As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProcessActionBase](topic9935.md)
    Dim value As Boolean
     
    value = instance.WillExecute  
  
C#|   
---|---  
      
    
    public virtual bool WillExecute {get;}  
  
#### Property Value

True if it this action wants to execute.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProcessActionBase Class](topic9935.md)   
[ProcessActionBase Members](topic9936.md)


