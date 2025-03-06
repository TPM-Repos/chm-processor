Specify Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications.Autopilot.Extensibility Namespace](topic1633.md) > [ISpecificationAutomation Interface](topic1761.md) : Specify Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_request_
    An instance of [ISpecificationRequest](topic1778.md) representing the data to be specified.

_waitForCompletion_
    True to wait for the specification to complete, false to queue the specification and return immediately.

Glossary Item Box

Starts a new specification based on the passed-in instance of [ISpecificationRequest](topic1778.md)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Sub Specify( _
       ByVal _request_ As [ISpecificationRequest](topic1778.md), _
       ByVal _waitForCompletion_ As Boolean _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISpecificationAutomation](topic1761.md)
    Dim request As [ISpecificationRequest](topic1778.md)
    Dim waitForCompletion As Boolean
     
    instance.Specify(request, waitForCompletion)  
  
C#|   
---|---  
      
    
    void Specify( 
       [ISpecificationRequest](topic1778.md) _request_ ,
       bool _waitForCompletion_
    )  
  
#### Parameters

 _request_
    An instance of [ISpecificationRequest](topic1778.md) representing the data to be specified.
_waitForCompletion_
    True to wait for the specification to complete, false to queue the specification and return immediately.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISpecificationAutomation Interface](topic1761.md)   
[ISpecificationAutomation Members](topic1762.md)


