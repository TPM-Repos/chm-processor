Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
Copy(SpecificationDetails,Boolean) Method   
  
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) > [SpecificationContext Class](topic11149.md) > [Copy Method](topic11161.md) : Copy(SpecificationDetails,Boolean) Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_specificationDetails_
    The details of the specification to clone.

_keepClosed_
    Whether or not to migrate the clone specification into the initial running state or not.

Glossary Item Box

Starts a new specification based on the given specification. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Public Overloads Sub Copy( _
       ByVal _specificationDetails_ As [SpecificationDetails](topic11292.md), _
       Optional ByVal _keepClosed_ As Boolean _
    )   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationContext](topic11149.md)
    Dim specificationDetails As [SpecificationDetails](topic11292.md)
    Dim keepClosed As Boolean
     
    instance.Copy(specificationDetails, keepClosed)  
  
C#|   
---|---  
      
    
    public void Copy( 
       [SpecificationDetails](topic11292.md) _specificationDetails_ ,
       bool _keepClosed_
    )  
  
#### Parameters

 _specificationDetails_
    The details of the specification to clone.
_keepClosed_
    Whether or not to migrate the clone specification into the initial running state or not.

# Exceptions

Exception| Description  
---|---  
[DriveWorks.ItemNotFoundException](topic3571.md)| The project, on which the specification was based, no longer exists.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationContext Class](topic11149.md)   
[SpecificationContext Members](topic11150.md)   
[Overload List](topic11161.md)


