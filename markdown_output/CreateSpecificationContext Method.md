Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateSpecificationContext Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [ISpecificationFactory Interface](topic471.md) : CreateSpecificationContext Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_environment_
    The settings which control the execution environment of the specification.

Glossary Item Box

Creates a new specification context using the given settings. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function CreateSpecificationContext( _
       ByVal _environment_ As [SpecificationEnvironment](topic11355.md) _
    ) As [SpecificationContext](topic11149.md)  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [ISpecificationFactory](topic471.md)
    Dim environment As [SpecificationEnvironment](topic11355.md)
    Dim value As [SpecificationContext](topic11149.md)
     
    value = instance.CreateSpecificationContext(environment)  
  
C#|   
---|---  
      
    
    [SpecificationContext](topic11149.md) CreateSpecificationContext( 
       [SpecificationEnvironment](topic11355.md) _environment_
    )  
  
#### Parameters

 _environment_
    The settings which control the execution environment of the specification.

#### Return Value

A specification context which represents the specification.

# Exceptions

Exception| Description  
---|---  
System.ArgumentNullException| One or more mandatory arguments were omitted.  
System.ArgumentOutOfRangeException| The specified group belongs to a different host.  
  
# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[ISpecificationFactory Interface](topic471.md)   
[ISpecificationFactory Members](topic472.md)


