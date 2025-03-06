![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxDeleteEventFlowConnection Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13091.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxDeleteEventFlowConnection Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_input_
    The input the connection is made to.

_output_
    The output part of the connection.

Glossary Item Box

Creates a new transaction that when executed will delete the given connection. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxDeleteEventFlowConnection( _
       ByVal _input_ As [InputEndpointRef](topic12893.md), _
       ByVal _output_ As [OutputEndpointRef](topic12921.md) _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim input As [InputEndpointRef](topic12893.md)
    Dim output As [OutputEndpointRef](topic12921.md)
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxDeleteEventFlowConnection(input, output)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxDeleteEventFlowConnection( 
       [InputEndpointRef](topic12893.md) _input_ ,
       [OutputEndpointRef](topic12921.md) _output_
    )  
  
#### Parameters

 _input_
    The input the connection is made to.
_output_
    The output part of the connection.

#### Return Value

A transaction which, when executed, will perform the operation.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)

©2024 DriveWorks Ltd. All Rights Reserved.
