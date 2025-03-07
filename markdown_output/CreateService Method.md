Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
CreateService Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [IServiceFactory Interface](topic429.md) : CreateService Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_type_
    The type representing the service to create.

Glossary Item Box

When implemented in a derived class, creates an instance of an object implementing the specified service type. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    Function CreateService( _
       ByVal _type_ As Type _
    ) As Object  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [IServiceFactory](topic429.md)
    Dim type As Type
    Dim value As Object
     
    value = instance.CreateService(type)  
  
C#|   
---|---  
      
    
    object CreateService( 
       Type _type_
    )  
  
#### Parameters

 _type_
    The type representing the service to create.

#### Return Value

An instance of an object implementing the specified service, or a null reference (Nothing in Visual Basic) if the specified type is not supported.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[IServiceFactory Interface](topic429.md)   
[IServiceFactory Members](topic430.md)


