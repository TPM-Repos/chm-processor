ValidateContext Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ICommandMonitor Interface](topic158.md) : ValidateContext Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_context_
    The context to validate.

Glossary Item Box

Validates the specified context is suitable for the command. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub ValidateContext( _
       ByVal _context_ As Object _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ICommandMonitor](topic158.md)
    Dim context As Object
     
    instance.ValidateContext(context)  
  
C#|   
---|---  
      
    
    void ValidateContext( 
       object _context_
    )  
  
#### Parameters

 _context_
    The context to validate.

# Exceptions

Exception| Description  
---|---  
[CommandContextInvalidException](topic671.md)| The supplied context is invalid.  
  
# Remarks

If the command does not expect context, and context is not a null reference (Nothing in Visual Basic), the implementation is expected to throw the [CommandContextInvalidException](topic671.md) exception.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICommandMonitor Interface](topic158.md)   
[ICommandMonitor Members](topic159.md)


