StartProfileEvent Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks Namespace](topic2159.md) > [ProjectProfiler Class](topic4712.md) : StartProfileEvent Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    

Glossary Item Box

Begins a new logical event scope in the profiler. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function StartProfileEvent( _
       ByVal _name_ As String _
    ) As IDisposable  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectProfiler](topic4712.md)
    Dim name As String
    Dim value As IDisposable
     
    value = instance.StartProfileEvent(name)  
  
C#|   
---|---  
      
    
    public IDisposable StartProfileEvent( 
       string _name_
    )  
  
#### Parameters

 _name_
    

#### Return Value

An object that when disposed will close (end) the event.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectProfiler Class](topic4712.md)   
[ProjectProfiler Members](topic4713.md)


