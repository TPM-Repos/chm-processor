![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeSpecificationProperty Method   
See Also [Send Feedback](mailto:apisupport@driveworks.co.uk?subject=Documentation Feedback: topic13008.md)  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeSpecificationProperty Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_specificationProperty_
    The specifiation property to change.

_newName_
    New name to apply to the property.

_rule_
    New rule to apply to the property.

_comment_
    Comment to apply to the property.

_index_
    New index to move the property to.

Glossary Item Box

Creates a transaction which, when commited, will Change the values of the given specification property. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeSpecificationProperty( _
       ByVal _specificationProperty_ As [ProjectSpecificationProperty](topic4853.md), _
       ByVal _newName_ As String, _
       ByVal _rule_ As String, _
       ByVal _comment_ As String, _
       ByVal _index_ As Integer _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim specificationProperty As [ProjectSpecificationProperty](topic4853.md)
    Dim newName As String
    Dim rule As String
    Dim comment As String
    Dim index As Integer
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeSpecificationProperty(specificationProperty, newName, rule, comment, index)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeSpecificationProperty( 
       [ProjectSpecificationProperty](topic4853.md) _specificationProperty_ ,
       string _newName_ ,
       string _rule_ ,
       string _comment_ ,
       int _index_
    )  
  
#### Parameters

 _specificationProperty_
    The specifiation property to change.
_newName_
    New name to apply to the property.
_rule_
    New rule to apply to the property.
_comment_
    Comment to apply to the property.
_index_
    New index to move the property to.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)

©2024 DriveWorks Ltd. All Rights Reserved.
