![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxCreateFormMessage Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13054.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxCreateFormMessage Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_code_
    The code to assign the new form message

_comment_
    

_rule_
    

Glossary Item Box

Creates a transaction which, when committed, will creates a form message with the given code number. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxCreateFormMessage( _
       ByVal _code_ As Integer, _
       ByVal _comment_ As String, _
       ByVal _rule_ As String _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim code As Integer
    Dim comment As String
    Dim rule As String
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxCreateFormMessage(code, comment, rule)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxCreateFormMessage( 
       int _code_ ,
       string _comment_ ,
       string _rule_
    )  
  
#### Parameters

 _code_
    The code to assign the new form message
 _comment_
    
_rule_
    

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)

©2024 DriveWorks Ltd. All Rights Reserved.
