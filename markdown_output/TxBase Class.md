TxBase Class   
[Members](topic13183.md)   
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Transactions Namespace](topic12835.md) : TxBase Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides a helper base class for transactions to automatically implement double-commit prevention. 

# Object Model

![](dotnetdiagramimages/image718.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public MustInherit Class TxBase 
       Inherits DriveWorks.DomainObject
       Implements [ITransaction](topic12837.md)   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [TxBase](topic13182.md)  
  
C#|   
---|---  
      
    
    public abstract class TxBase : DriveWorks.DomainObject, [ITransaction](topic12837.md)    
  
# Inheritance Hierarchy

System.Object  
System.MarshalByRefObject  
**DriveWorks.Transactions.TxBase**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[TxBase Members](topic13183.md)   
[DriveWorks.Transactions Namespace](topic12835.md)


