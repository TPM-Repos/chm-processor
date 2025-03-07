Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CheckStopped Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.GroupMaintenance Namespace](topic9628.md) > [CopyGroupProcess Class](topic9776.md) : CheckStopped Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Checks to see if the process is canceled. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CheckStopped() As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [CopyGroupProcess](topic9776.md)
    Dim value As Boolean
     
    value = instance.CheckStopped()  
  
C#|   
---|---  
      
    
    public bool CheckStopped()  
  
#### Return Value

If the process is canceled.

# Remarks

This will cancel the operation if it is marked for cancellation.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[CopyGroupProcess Class](topic9776.md)   
[CopyGroupProcess Members](topic9777.md)


