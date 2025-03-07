Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxCreateEventFlowConnection Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxCreateEventFlowConnection Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_input_
    The input to connect to the output.

_output_
    The output to connect to the input.

Glossary Item Box

Creates a new transaction that when executed will create a connection between the given endpoints. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxCreateEventFlowConnection( _
       ByVal _input_ As [InputEndpointRef](topic12893.md), _
       ByVal _output_ As [OutputEndpointRef](topic12921.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim input As [InputEndpointRef](topic12893.md)
    Dim output As [OutputEndpointRef](topic12921.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxCreateEventFlowConnection(input, output)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxCreateEventFlowConnection( 
       [InputEndpointRef](topic12893.md) _input_ ,
       [OutputEndpointRef](topic12921.md) _output_
    )  
  
#### Parameters

 _input_
    The input to connect to the output.
_output_
    The output to connect to the input.

#### Return Value

A transaction which, when executed, will perform the operation.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


