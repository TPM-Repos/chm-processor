       

 Collapse All Expand All  Language Filter: All  Language Filter: Multiple  Language Filter: Visual Basic (Declaration) Language Filter: Visual Basic (Usage) Language Filter: C#  
---  
DriveWorks SDK Documentation  |   
---|---  
SpecificationDetails Class   
[Members](topic11293.md)   
[DriveWorks.Engine Assembly](topic2156.md) > [DriveWorks.Specification Namespace](topic10764.md) : SpecificationDetails Class  
---  
  
Visual Basic (Declaration)    
Visual Basic (Usage)    
C# 

Glossary Item Box

Provides information about a registered DriveWorks specification. 

# Object Model

![](dotnetdiagramimages/image572.png)

# Syntax

Visual Basic (Declaration)|   
---|---  
      
    
    <DebuggerDisplayAttribute(Value="{Name}", 
       Name="", 
       Type="", 
       Target=, 
       TargetTypeName="")>
    <KnownTypeAttribute(MethodName="", Type=System.String[])>
    <SerializableAttribute()>
    Public NotInheritable Class SpecificationDetails   
  
Visual Basic (Usage)| Copy Code  
---|---  
      
    
    Dim instance As [SpecificationDetails](topic11292.md)  
  
C#|   
---|---  
      
    
    [DebuggerDisplayAttribute(Value="{Name}", 
       Name="", 
       Type="", 
       Target=, 
       TargetTypeName="")]
    [KnownTypeAttribute(MethodName="", Type=System.String[])]
    [SerializableAttribute()]
    public sealed class SpecificationDetails   
  
# Remarks

Modifications made to an instance of SpecificationDetails are not immediately reflected in the group from which the instance was obtained. To apply any modifications, call the **DriveWorks.GroupSpecifications.TryUpdateSpecification** method.

# Inheritance Hierarchy

System.Object  
**DriveWorks.Specification.SpecificationDetails**  


# Requirements

**Target Platforms:** Please see DriveWorks software prerequisites.

# See Also

#### Reference

[SpecificationDetails Members](topic11293.md)   
[DriveWorks.Specification Namespace](topic10764.md)


