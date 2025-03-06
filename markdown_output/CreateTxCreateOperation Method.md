![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxCreateOperation Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13055.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxCreateOperation Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_stateTitle_
    The state to create this operation in.

_name_
    The name and title of the new operation

Glossary Item Box

Creates a transaction which, when committed, will create an operation with given name on the given state. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxCreateOperation( _
       ByVal _stateTitle_ As String, _
       ByVal _name_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim stateTitle As String
    Dim name As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxCreateOperation(stateTitle, name)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxCreateOperation( 
       string _stateTitle_ ,
       string _name_
    )  
  
#### Parameters

 _stateTitle_
    The state to create this operation in.
_name_
    The name and title of the new operation

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)

©2024 DriveWorks Ltd. All Rights Reserved.
