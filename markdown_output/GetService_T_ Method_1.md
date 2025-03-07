_T_
    The type of service to retrieve.

Collapse All Expand All Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
GetService<T> Method   
  
[DriveWorks.Applications Assembly](topic13.md) > [DriveWorks.Applications Namespace](topic16.md) > [Extensions Class](topic814.md) : GetService<T> Method  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

_serviceProvider_
    The service provider from which to get the service.

Glossary Item Box

Gets the specified service from the given service provider. 

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <ExtensionAttribute()>
    Public Shared Function GetService(Of T)( _
       ByVal _serviceProvider_ As IServiceProvider _
    ) As T  
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim serviceProvider As IServiceProvider
    Dim value As T
     
    value = [Extensions](topic814.md).GetService(Of T)(serviceProvider)  
  
C#|   
---|---  
      
    
    [ExtensionAttribute()]
    public static T GetService<T>( 
       IServiceProvider _serviceProvider_
    )  
  
#### Parameters

 _serviceProvider_
    The service provider from which to get the service.

#### Type Parameters

_T_
    The type of service to retrieve.

#### Return Value

A service of the specified type, or the default value for the specified type if the service isn't available.

# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[Extensions Class](topic814.md)   
[Extensions Members](topic815.md)


