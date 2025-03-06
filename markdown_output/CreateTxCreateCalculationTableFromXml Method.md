![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/collapse.gif) ![](dotnetimages/expand.gif) ![](dotnetimages/drpdown.gif) ![](dotnetimages/drpdown_orange.gif) ![](dotnetimages/copycode.gif) ![](dotnetimages/copycodeHighlight.gif)

![](dotnetimages/collapse.gif) Collapse All Expand All ![](dotnetimages/drpdown.gif) Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxCreateCalculationTableFromXml Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxCreateCalculationTableFromXml Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_calculationTableXml_
    The System.Xml.Linq.XElement representing the calculation table to create.

Glossary Item Box

Creates a transaction that will create a calculation table from the supplied XML element. 

# ![](dotnetimages/collapse.gif)Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxCreateCalculationTableFromXml( _
       ByVal _calculationTableXml_ As XElement _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| ![](dotnetimages/copycode.gif)Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim calculationTableXml As XElement
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxCreateCalculationTableFromXml(calculationTableXml)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxCreateCalculationTableFromXml( 
       XElement _calculationTableXml_
    )  
  
#### Parameters

 _calculationTableXml_
    The System.Xml.Linq.XElement representing the calculation table to create.

#### Return Value

A transaction that will perform the operation.

# ![](dotnetimages/collapse.gif)Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# ![](dotnetimages/collapse.gif)See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


