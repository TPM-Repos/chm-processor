Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateTxChangeFormControlPropertyExtendedValue Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) > [ProjectTransactionFactory Class](topic12928.md) : CreateTxChangeFormControlPropertyExtendedValue Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_control_
    Control the property belongs to.

_dynamicProperty_
    Property to change.

_isExtended_
    Determines whether the property will be extended or unextended.

Glossary Item Box

Creates a transaction to either extend or unextend a [DriveWorks.Forms.DataModel.DynamicProperty](topic9398.md). 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Function CreateTxChangeFormControlPropertyExtendedValue( _
       ByVal _control_ As [ControlBase](topic7698.md), _
       ByVal _dynamicProperty_ As [DynamicProperty](topic9398.md), _
       ByVal _isExtended_ As Boolean _
    ) As [ITransaction](topic12837.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ProjectTransactionFactory](topic12928.md)
    Dim control As [ControlBase](topic7698.md)
    Dim dynamicProperty As [DynamicProperty](topic9398.md)
    Dim isExtended As Boolean
    Dim value As [ITransaction](topic12837.md)
     
    value = instance.CreateTxChangeFormControlPropertyExtendedValue(control, dynamicProperty, isExtended)  
  
C#|   
---|---  
      
    
    public [ITransaction](topic12837.md) CreateTxChangeFormControlPropertyExtendedValue( 
       [ControlBase](topic7698.md) _control_ ,
       [DynamicProperty](topic9398.md) _dynamicProperty_ ,
       bool _isExtended_
    )  
  
#### Parameters

 _control_
    Control the property belongs to.
_dynamicProperty_
    Property to change.
_isExtended_
    Determines whether the property will be extended or unextended.

#### Return Value

A transaction.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ProjectTransactionFactory Class](topic12928.md)   
[ProjectTransactionFactory Members](topic12929.md)


