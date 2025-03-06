SetIsDynamic Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Components.Tasks Namespace](topic6391.md) > [ComponentTaskProperty Class](topic6633.md) : SetIsDynamic Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_isDynamic_
    True if this property should be bound to a rule, False for it to be bound to a static value.

Glossary Item Box

Changes whether this property is bound to a rule, or a static value. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Sub SetIsDynamic( _
       ByVal _isDynamic_ As Boolean _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ComponentTaskProperty](topic6633.md)
    Dim isDynamic As Boolean
     
    instance.SetIsDynamic(isDynamic)  
  
C#|   
---|---  
      
    
    public void SetIsDynamic( 
       bool _isDynamic_
    )  
  
#### Parameters

 _isDynamic_
    True if this property should be bound to a rule, False for it to be bound to a static value.

# Exceptions

Exception| Description  
---|---  
System.InvalidOperationException| The property does not support being made dynamic.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ComponentTaskProperty Class](topic6633.md)   
[ComponentTaskProperty Members](topic6634.md)


