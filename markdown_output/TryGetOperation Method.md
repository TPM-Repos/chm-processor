TryGetOperation Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [Operations Class](topic11095.md) : TryGetOperation Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_name_
    The name of the operation to get.

_operation_
    Receives the operation.

Glossary Item Box

Gets the operation with the specified name. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function TryGetOperation( _
       ByVal _name_ As String, _
       ByRef _operation_ As [Operation](topic11068.md) _
    ) As Boolean  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [Operations](topic11095.md)
    Dim name As String
    Dim operation As [Operation](topic11068.md)
    Dim value As Boolean
     
    value = instance.TryGetOperation(name, operation)  
  
C#|   
---|---  
      
    
    public bool TryGetOperation( 
       string _name_ ,
       ref [Operation](topic11068.md) _operation_
    )  
  
#### Parameters

 _name_
    The name of the operation to get.
_operation_
    Receives the operation.

#### Return Value

True if the operation was found and returned, otherwise false.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Operations Class](topic11095.md)   
[Operations Members](topic11096.md)


