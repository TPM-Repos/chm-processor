Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Invoke Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ICommand Interface](topic77.md) : Invoke Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_context_
    Contextual data required for the operation to proceed.

Glossary Item Box

Invokes the operation represented by the command. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub Invoke( _
       ByVal _context_ As Object _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ICommand](topic77.md)
    Dim context As Object
     
    instance.Invoke(context)  
  
C#|   
---|---  
      
    
    void Invoke( 
       object _context_
    )  
  
#### Parameters

 _context_
    Contextual data required for the operation to proceed.

# Exceptions

Exception| Description  
---|---  
[CommandInvocationException](topic681.md)| Thrown when there is any error during invocation.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ICommand Interface](topic77.md)   
[ICommand Members](topic78.md)


