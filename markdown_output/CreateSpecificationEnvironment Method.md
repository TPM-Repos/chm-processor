Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateSpecificationEnvironment Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ISpecificationFactory Interface](topic471.md) : CreateSpecificationEnvironment Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Creates the default specification environment for the application. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function CreateSpecificationEnvironment() As [SpecificationEnvironment](topic11355.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISpecificationFactory](topic471.md)
    Dim value As [SpecificationEnvironment](topic11355.md)
     
    value = instance.CreateSpecificationEnvironment()  
  
C#|   
---|---  
      
    
    [SpecificationEnvironment](topic11355.md) CreateSpecificationEnvironment()  
  
# Remarks

The returned specification environment may be locked from further changes.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISpecificationFactory Interface](topic471.md)   
[ISpecificationFactory Members](topic472.md)


